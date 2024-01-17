export interface FileInfo {
    name: string;
    size: string;
    file_type: string;
}

export interface ProjectInfo {
    project_id: string;
    slug: string;
    name: string;
    created_at: string;
    last_edited: string;
    size: string;
    onDelete: (slug: string) => void;
}

export interface funcProp {
    func: (data: string) => void;
}

export interface removeNavBarFuncProp{
    removeNavBar: () => void;
}
