import React from 'react';
import { Switch, Route, Link } from 'react-router-dom';
import 'bootstrap/dist/css/bootstrap.min.css';

import TodosList from './components/todo-list';
import AddTodo from './components/add-todo';
import Login from './components/login';
import Signup from './components/signup';

import Nav from 'react-bootstrap/Nav';
import Navbar from 'react-bootstrap/Navbar';
import Container from 'react-bootstrap/Container';

function App(){

  const [user, setUser] = React.useState(null);
  const [token, setToken] = React.useState(null);
  const [error, setError] = React.useState('');

  async function login(user = null){
    setUser(user);
  }

  async function logout(){
    setUser(null);
  }

  async function signup(user = null){
    setUser(user);
  }

  return (
    <div className='App'>
      <Navbar bg="primary" variant="dark">
        <div className="container-fluid">
          <Navbar.Brand>Todos App</Navbar.Brand>
          <Nav className="me-auto">
            <Container>
              <Link className="nav-link" to={"/todos"}></Link>
              { user ? (
                <Link className="nav-link">Logout ({user})</Link>
              ) : (
                <>
                  <Link className="nav-link" to={"/login"}>Login</Link>
                  <Link className="nav-link" to={"/signup"}>Signup</Link>
                </>
              )}
            </Container>
          </Nav>
        </div>
      </Navbar>
    </div>
  )
}

export default App;
