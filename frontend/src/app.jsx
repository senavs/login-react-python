import { BrowserRouter as Router, Switch, Route } from 'react-router-dom'

import NavBar from './components/navbar'
import Home from './components/home'
import Login from './components/login'
import SignIn from './components/signin'
import Public from './components/public'
import Private from './components/private'
import { PrivateRoute } from './utils/routes'
import { AuthProvider } from './utils/providers'


const App = () => {

  // render
  return (
    <Router>
      <Switch>
        <AuthProvider>
          <NavBar>
            <Route exact={true} path='/' component={Home} />
            <Route exact={true} path='/login' component={Login} />
            <Route exact={true} path='/signin' component={SignIn} />
            <Route exact={true} path='/public' component={Public} />
            <PrivateRoute exact={true} path='/private' component={Private} />
          </NavBar>
        </AuthProvider>
      </Switch>
    </Router>
  )

}

export default App