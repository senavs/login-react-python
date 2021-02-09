import { useState } from 'react'

import Storage from '../services/storage'


export const useStorage = (key) => {

  const [state, setState] = useState(Storage.get(key))

  const setter = (value) => {
    Storage.post(key, value)
    setState(value)
  }

  const deleter = () => {
    Storage.delete(key)
    setState(Storage.get(key))
  }

  return [state, setter, deleter]

}