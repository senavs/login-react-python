import { useState, useContext } from "react"
import { Redirect, useHistory } from 'react-router-dom'

import { AuthContext } from '../utils/providers'
import AuthService from '../services/auth'


const SignIn = () => {
  // contexts
  const { auth, setAuth } = useContext(AuthContext)
  const history = useHistory()

  // states
  const [form, setForm] = useState(() => ({ username: '', password: '' }))
  const [formText, setFormText] = useState('')

  // functions
  const formHandler = (event) => {
    const { name, value } = event.target
    setForm({
      ...form,
      [name]: value
    })
  }

  const signin = (event) => {
    event.preventDefault()
    const { username, password } = form
    setFormText('')
    setForm({ username: '', password: '' })
    AuthService.register(username, password)
      .then((res) => {
        setAuth(res)
        history.push('/')
      })
      .catch((err) => {
        setFormText(err.message)
      })

  }

  // if user is already logedin, send to home page
  if (auth.token) {
    return <Redirect to='/' />
  }

  // render
  return (
    <div className="container">
      <h1 className="text-center">Sign In</h1>
      <form className="form border bolder-2 border-info rounded rounded-3 p-3" onSubmit={signin}>
        <div className="row mb-2">
          <div className="col-md-2 my-auto">
            <label className="form-label">Username</label>
          </div>
          <div className="col-md-10">
            <input className="form-control" type="text" maxLength="32" name="username" value={form.username} onChange={formHandler} required></input>
          </div>
        </div>
        <div className="row mb-2">
          <div className="col-md-2 my-auto">
            <label className="form-label">Passoword</label>
          </div>
          <div className="col-md-10">
            <input className="form-control" type="password" name="password" value={form.password} onChange={formHandler} required></input>
          </div>
        </div>
        <div className="row">
          <small className={"form-text text-center " + (formText ? "text-danger" : "")}>{formText || "Fill the form to register"}</small>
        </div>
        <div className="row">
          <div className="col-10 offset-1 col-md-4 offset-md-4">
            <div className="row">
              <button type="submit" className="btn btn-info">Register</button>
            </div>
          </div>
        </div>
      </form>
    </div>
  )

}

export default SignIn