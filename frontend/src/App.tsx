import { useState } from 'react';

import {
    BrowserRouter as Router,
    Routes,
    Route,
} from 'react-router-dom';

import globalStyles from './App.module.css';

import Landing from './components/core/landing/Landing';
import Editor from './components/core/editor/Editor';
import Navbar from './components/shared/navigation-bar/Navbar';
import CreatePodcast from './components/core/create-project/CreatePodcast';
import Login from './components/features/log-in/Login';

function App() {

    const [navbarTitle, setNavbarTitle] = useState("Podplistic");

    const updateNavbarTitle = (data: string) => {
        setNavbarTitle(data);
    };

    const [showNavBar,setShowNavBar] = useState(true);

    const disableNavBar = () => {
        setShowNavBar(false);
    };

    return (
        <div className={globalStyles.App}>
            <Router>
                {showNavBar && <Navbar title={navbarTitle}></Navbar>}
                <div className={globalStyles.mainContent}>
                    <Routes>
                        <Route path="/" element={<Landing func={updateNavbarTitle} />} />
                        <Route path="editor/:controller_type/:project_id" element={<Editor func={updateNavbarTitle} />} />
                        <Route path="create" element={<CreatePodcast />} />
                        <Route path="login" element={<Login  removeNavBar={disableNavBar} />} />
                    </Routes>
                </div>
            </Router>
        </div>
    );
}

export default App;
