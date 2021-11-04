import React from "react";
import { Route, Switch } from "react-router";
import "./App.css";
import Home from "./screens/Home";
import LogIn from "./screens/LogIn";
import Profile from "./screens/Profile";
import UserProfile from "./screens/UserProfile";

function App() {
  return (
    <div className="App">
      <Switch>
        <Route exact path="/">
          <Home />
        </Route>
        <Route path="/login">
          <LogIn />
        </Route>
        <Route path="/profile">
          <Profile />
        </Route>
        <Route path="/user/:id">
          <UserProfile />
        </Route>
      </Switch>
    </div>
  );
}

export default App;
