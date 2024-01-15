from flask import Blueprint, jsonify, request
from datetime import datetime

from db import db
from api.models.project import Project

bp = Blueprint('project_routes', __name__)

@bp.route('/project/<project_id>', methods=['GET'])
def get_single_project(project_id):
    """
    Fetches metadata on one project.
    :param project_id: the id of the project to be fetched.
    """
    try:
        project = Project.query.get(project_id)
        if not project:
            return jsonify({'error': 'Project not found'}), 404
        response = jsonify(project.toJSON())
        response.headers.add('Access-Control-Allow-Origin', '*')
        return response, 200

    except Exception as e:
        error_message = f'Error retrieving projects: {str(e)}'
        return jsonify({'error': error_message}), 500  


@bp.route('/projects', methods=['GET'])
def get_projects():
    try:
        projects = Project.query.all()
        projects = [project.toJSON() for project in projects]
        response = jsonify(projects)
        response.headers.add('Access-Control-Allow-Origin', '*')
        return response, 200

    except Exception as e:
        error_message = f'Error retrieving projects: {str(e)}'
        return jsonify({'error': error_message}), 500


@bp.route('/create/<project_name>', methods=['POST'])
def create_project(project_name):
    """
    Endpoint to be used when creating a new project.
    :param project_name: the name of the project to be created.
    :return result: if unsuccessful return error code, if successful return id of new project.
    """
    try:
        new_project = Project(name=project_name)
        db.session.add(new_project)
        db.session.commit()
        project = Project.query.filter_by(project_id=new_project.project_id).first()
    
    except Exception as e:
        error_message = f'Error connecting to the database: {str(e)}'
        return jsonify({'error': error_message}), 500

    else:
        result = {'message': 'Database connection successful', 'project_id': project.project_id, 'name': project.name}
        return jsonify(result), 200


@bp.route('/delete/<project_id>', methods=['POST'])
def delete_project(project_id):
    """
    Endpoint to be used when deleting a project.
    :param project_id: the id of the project to be deleted. This is used as it is the PK in the projects table
    """
    try:
        project = Project.query.get(project_id)
        if not project:
            return jsonify({'error': 'Project not found'}), 404
        db.session.delete(project)
        db.session.commit()

    except Exception as e:
        error_message = f'Error connecting to the database: {str(e)}'
        return jsonify({'error': error_message}), 500

    else:
        result = {'message': 'Project deleted successfully'}
        return jsonify(result), 200    

@bp.route('/update/<project_id>', methods=['GET'])
def update_last_edited(project_id):
    """
    Sets the last_edited field to whatever the current time is.
    :param project_id: the id of the project to be updated.
    """
    try:
        project = Project.query.get(project_id)
        if not project:
            return jsonify({'error': 'Project not found'}), 404
        project.last_edited = datetime.utcnow()
        db.session.commit()

    except Exception as e:
        error_message = f'Error connecting to the database: {str(e)}'
        return jsonify({'error': error_message}), 500

    else:
        result = {'message': 'Last edited updated successfully'}
        return jsonify(result), 200    