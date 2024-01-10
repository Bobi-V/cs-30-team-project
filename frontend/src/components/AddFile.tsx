import FileComponent from "./FileComponent";
import { FileInfo } from "../Interfaces"
import styles from "./AddFile.module.css"
import { PropsWithChildren } from "react";

const AddFile:React.FC<PropsWithChildren<any>> = (props) => {
    return (
            <div id={styles.fileAdd}>
                <div className={styles.projectName}>
                    <p> Name of project </p>
                    <input type="text" onChange={props.changeProjectName} />
                </div>
                <div className={styles.dragFiles}>
                    <p className={styles.dragChild}> Drag and drop to add files </p>
                    <input type="file" id="files" accept="video/*, audio/*" className={`${styles.dragChild} ${styles.fileUpload}`} ref={props.inputFile} onChange={props.uploadFile} title=" "/>
                </div>
                <div className={styles.filesText}>
                    <p> Uploaded Files </p>
                </div>
                <div className={styles.uploadedFiles}>
                    {props.files.map((props: FileInfo) => {
                        return (
                            <FileComponent slug={props.slug} name={props.name} date={props.date} size={props.size} />
                        )
                    })}
                </div>
            </div>
    )
}

export default AddFile;
