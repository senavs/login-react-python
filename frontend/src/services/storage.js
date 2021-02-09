export default class Storage {
  
  static get(key, defaultReturn={}) {
    return JSON.parse(localStorage.getItem(key)) || defaultReturn
  }

  static post(key, value, useParse=true) {
    let newValue = useParse ? JSON.stringify(value) : value

    return localStorage.setItem(key, newValue)
  }

  static delete(key) {
    return localStorage.removeItem(key)
  }

}