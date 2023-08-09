import React, { useState } from 'react';
import {
  BrowserRouter,
  Routes,
  Route
} from "react-router-dom";

import Login from './components/Login/login';
import Processors from './components/processors';


function App() {
  const [token, setToken] = useState();

  if(!token) {
    return <Login setToken={setToken} />
  }

  return (
    <div className='wrapper'>
      <h1>Hello!</h1>
      <BrowserRouter>
        <Routes>
          <Route
            path="/processors"
            element = {<Processors />}
          />
        </Routes>
    </BrowserRouter>
    </div>
  );
}

export default App;
