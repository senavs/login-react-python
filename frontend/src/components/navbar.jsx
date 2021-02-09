import { useContext } from 'react'
import { useHistory } from 'react-router-dom'

import { AuthContext } from '../utils/providers'
import AuthService from '../services/auth'


const NavBar = ({ children }) => {
  // contexts
  const { auth, removeAuth } = useContext(AuthContext)
  const history = useHistory()

  // functions
  const logout = () => {
    AuthService.logout(auth.token).then(() => {
      removeAuth()
      history.push('/')
    }).catch(removeAuth)
  } 

  // render
  return (
    <div>
      <nav className="navbar navbar-expand-md navbar-light bg-info">
        <div className="container-fluid">
          {/* brand */}
          <a className="navbar-brand fs-3" href="/">ReactPy</a>

          {/* toggler button */}
          <button className="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
            <span className="navbar-toggler-icon"></span>
          </button>

          {/* nav links */}
          <div className="collapse navbar-collapse" id="navbarNav">
            {/* left links */}
            <ul className="navbar-nav">
              <li className="nav-item fs-5">
                <a className="nav-link" href="/">Home</a>
              </li>
              <li className="nav-item fs-5">
                <a className="nav-link" href="/public">Public</a>
              </li>
              <li className="nav-item fs-5">
                <a className="nav-link" href="/private">Private</a>
              </li>
            </ul>

            {/* right links */}
            <ul className="navbar-nav ms-auto">
              <li className="nav-item fs-5">
                {!auth.token && <a className="nav-link" href="/login">Login</a>}
              </li>
              <li className="nav-item fs-5">
                {!auth.token
                  ? <a className="nav-link" href="/signin">Sign in</a>
                  : <a className="nav-link" href="/#" onClick={logout}>Logout</a>
                }
              </li>
            </ul>
          </div>
        </div>
      </nav>
      <div className="container mt-5">
        {children}
      </div>
    </div>
  )

}

export default NavBar