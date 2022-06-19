<h1 align="center">10Acadamy's training Certificate Generation, Distribution, and Value Transfer with Algorand NFTs and Smart-Contracts</h1>
<div>
<a href="https://github.com/Hen0k/tenx-cert-gen-dApp"><img src="https://img.shields.io/github/forks/Hen0k/tenx-cert-gen-dApp" alt="Forks Badge"/></a>
<a "https://github.com/Hen0k/tenx-cert-gen-dApp/pulls"><img src="https://img.shields.io/github/issues-pr/Hen0k/tenx-cert-gen-dApp" alt="Pull Requests Badge"/></a>
<a href="https://github.com/Hen0k/tenx-cert-gen-dApp/issues"><img src="https://img.shields.io/github/issues/Hen0k/tenx-cert-gen-dApp" alt="Issues Badge"/></a>
<a href="https://github.com/Hen0k/tenx-cert-gen-dApp/graphs/contributors"><img alt="GitHub contributors" src="https://img.shields.io/github/contributors/Hen0k/tenx-cert-gen-dApp?color=2b9348"></a>
<a href="https://github.com/Hen0k/tenx-cert-gen-dApp/blob/main/LICENCE"><img src="https://img.shields.io/github/license/Hen0k/tenx-cert-gen-dApp?color=2b9348" alt="License Badge"/></a>
</div>
</br>

# tenx-cert-gen-dApp


## Problem Description

I’m building a system that would allow 10 Academy to mint and distribute NFT
certifications to its trainees once they fulfill the requirements. I will need a front-end where the team from 10 Academy would verify trainees, where trainees would opt-in for the NFTs. A back-end system that would handle most of the logic and a blockchain that would allow me to mint and assign ownership of the NFTs to the students. I will be using Algorand for my blockchain, Flask for the back-end, and ReactJS for the front-end. Next, I will explore what each component would handle.

The front-end will allow all users (trainees and staff) to authenticate using an email and a password. Once logged in, a person connects their wallet. They would then be presented a view corresponding to the role their public key or email is assigned. Staff members can receive opt-in requests from the trainees and approve or decline the requests for the certifications based on some criteria. If a trainee fulfills the criteria they (the staff) can mint and send them their NFT. For the trainee, the front-end would allow them to place their opt-in request and monitor the status of their request.

The backend handles the business logic of the app. This includes identifying the roles of the users and allowing the staff to mint the NFTs and distribute them. It will take requests from the front-end and also make requests to the blockchain. There is also a database for holding the user credentials and trainees’ status.

## Repository Structure
```bash
> tree -L 2
.
├── backend
│   ├── config.py
│   ├── flask_app
│   ├── __pycache__
│   ├── README.md
│   ├── requirements.txt
│   ├── run_app.sh
│   └── wsgi.py
├── frontend
│   ├── package.json
│   ├── package-lock.json
│   ├── public
│   ├── README.md
│   ├── src
├── LICENSE
├── README.md
```

## Installation Instructions

1. clone the repo
   ```bash
   git clone https://github.com/Hen0k/tenx-cert-gen-dApp.git
   ```
2. move into the backend folder and run the following lines in your terminal
   ```bash
   cd backend
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ./run_app
   ```
3. For the frontend, move into the frontend directory and then install all the dependecies using the following line.
    ```bash
    npm install
    ```
4. run the react app using
    ```bash
    npm start
    ```

## Smart Contract logic

**Coming Soon**