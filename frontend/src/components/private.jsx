import { useContext } from "react"

import { AuthContext } from '../utils/providers'


const Private = () => {
  // contexts
  const { auth } = useContext(AuthContext)

  // render
  return (
    <div className="container">
      <div className="row">
        <h1>Private page</h1>
        <p>Wellcome to the private room <strong>{auth.user ? auth.user.username : "Mr Error"}</strong>!!</p>
      </div>
      <div className="row">
        <p>If you are seeing this page, it means that you are logged and the project works.</p>
        <p>Thank you!!</p>
      </div>
    </div>
  )

}

export default Private