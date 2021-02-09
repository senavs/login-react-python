import { createContext, useEffect } from 'react'

import AuthService from '../services/auth'
import { useStorage } from './hooks'


export const AuthContext = createContext({})

export const AuthProvider = ({ children }) => {
  // events
  const [auth, setAuth, removeAuth] = useStorage('auth')

  // effects
  useEffect(() => {
    if (auth.token) {
      AuthService.validate(auth.token).then(setAuth).catch(removeAuth)
    } else {
      removeAuth()
    }
  }, [])

  // render
  return (
    <AuthContext.Provider value={{ auth, setAuth, removeAuth }}>
      { children}
    </AuthContext.Provider>
  )
}
