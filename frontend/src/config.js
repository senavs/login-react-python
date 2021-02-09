const config = {
  urls: {
    auth: {
      login: process.env.LOGIN_URL || 'http://0.0.0.0:8081/auth/login',
      logout: process.env.LOGOUT_URL || 'http://0.0.0.0:8081/auth/logout',
      validate: process.env.VALIDATE_URL || 'http://0.0.0.0:8081/auth/validate',
      register: process.env.VALIDATE_URL || 'http://0.0.0.0:8081/auth/register'
    }
  }
}

export default config