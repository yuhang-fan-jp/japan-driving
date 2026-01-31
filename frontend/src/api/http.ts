import axios from "axios"

const http = axios.create({
  baseURL: "http://127.0.0.1:8000",
  timeout: 10000,
})

/*
 * 请求拦截器：自动带 token
 */
http.interceptors.request.use(
  (config) => {
    const token = localStorage.getItem("token")
    if (token) {
      config.headers.Authorization = `Bearer ${token}`
    }
    return config
  },
  (error) => {
    return Promise.reject(error)
  }
)

/*
 * 响应拦截器：统一处理 401
 */
http.interceptors.response.use(
  (response) => response,
  (error) => {
    if (error.response?.status === 401) {
      // token 失效 / 未登录
      localStorage.removeItem("token")
      window.location.href = "/login"
    }
    return Promise.reject(error)
  }
)

export default http

http.interceptors.request.use((config) => {
  const token = localStorage.getItem("token")
  console.log("request token =", token)
  if (token) {
    config.headers.Authorization = `Bearer ${token}`
  }
  return config
})