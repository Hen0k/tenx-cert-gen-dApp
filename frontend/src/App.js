import './App.css';
import React from 'react';
import PopupPermissions from './components/landingPage/PopupPermissions'
import Header from './components/landingPage/headerBar';
function App() {
  return (
    <div className="App">
      <Header />
      <h1>Welcome to 10 Academy's NFT certificates minter and distributor</h1>
      <PopupPermissions />
    </div>
  );
}

export default App;
