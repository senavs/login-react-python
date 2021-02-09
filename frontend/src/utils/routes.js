import React, { useContext } from 'react'
import { Route, Redirect } from 'react-router-dom'

import { AuthContext } from '../utils/providers'


export const PrivateRoute = ({ component: Component, ...rest }) => {
  const { auth } = useContext(AuthContext)

  return (
    <Route
      {...rest}
      render={() => (Object.keys(auth).length !== 0) ? <Component {...rest} /> : <Redirect to="/login" />}
    />
  )

}
