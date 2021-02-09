import { useContext } from "react"

import { AuthContext } from '../utils/providers'


const Public = () => {
  // contexts
  const { auth } = useContext(AuthContext)

  // render
  return (
    <div className="container">
      <div className="row">
        <h1>Public page</h1>
        <p>Wellcome to the public room!!</p>
        {auth.user
          ? <p className="text-success">You are logged in as <strong>{auth.user ? auth.user.username : "Mr Error"}</strong></p>
          : <p className="text-secondary">Login if you whant to see your name here</p>}
      </div>
      <div className="row">
        <p>If you are seeing this page, it means that you are logged and the project works.</p>
        <p>Thank you!!</p>
      </div>
    </div>
  )

}

export default Public