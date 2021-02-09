import axios from 'axios'

import config from '../config'


export default class AuthService {

  static async login(username, password) {
    try {
      const response = await axios.post(config.urls.auth.login, { username, password })
      return response.data
    } catch (error) {
      throw error.response.data
    }
  }

  static async logout(token) {
    try {
      const response = await axios.post(config.urls.auth.logout, null, { headers: { Authenticate: `Bearer ${token}` } })
      return true ? response.request.status : false
    } catch (error) {
      return false
    }
  }

  static async validate(token) {
    try {
      const response = await axios.post(config.urls.auth.validate, null, { headers: { Authenticate: `Bearer ${token}` } })
      return response.data
    } catch (error) {
      return error.response.data
    }
  }

  static async register(username, password) {
    try {
      const response = await axios.post(config.urls.auth.register, { username, password })
      return response.data
    } catch (error) {
      return error.response.data
    }
  }

}
