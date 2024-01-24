# CS30 Main - Podplistic Podcast Editor

<img src="https://static.wixstatic.com/media/4ae805_8f7ae020838c4a47adbf40181bf111d1~mv2.png/v1/fill/w_558,h_156,al_c,q_85,usm_0.66_1.00_0.01,enc_auto/Podplistic%20Logo%20PNG_edited.png" align="right"
     alt="Podplistic Logo" height="50">



This repository contains the code for the Podplistic Podcast Editor, a project created by University of Glasgow students as part of the third-year group project. The aim of this project is to develop an MVP for Podplistic to use to raise additional finance to further develop the application. 

Major features include:
- [x] Importing multimedia files
- [ ] Syncing different audio and video sources
- [ ] User-controlled trimming and clipping
- [ ] Podcast export options
- [ ] Automatic removal of 'dead sections' (and user ability to tweak)
- [ ] Automatic audio mastering (and user ability to tweak)
- [ ] Persistent video editing sessions
- [x] Dummy login page

A key aim of the project is to create an application that is accessible to users of multiple skill levels. As such, many features must have an automatic mode (handled entirely by the application) **as well as** the ability for more experienced users to manually tweak their work.

## Installation
### Frontend
After cloning the repo, move to the `frontend` directory and run `npm start`.\
If you don't have `npm` installed, you will need to run this: `sudo apt install npm`.\
If you haven't got all of the `npm` dependencies, run `npm install`.\
Try `npm start` again and the website should launch in your browser.

### Backend 
Install Docker.\
Once Docker is installed, run `docker compose up` from the project's root directory.\
Everything should now work!

## Project Dependencies

## Authors
Jamie Robb, Ewan Hibberd, Boris Velinov, Michael Anderson, Miko Osak, Arif Yakupogullari