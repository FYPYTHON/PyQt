import axios from 'axios'
// import fsm from '../main'

if (process.env.API_ROOT === '' && process.env.NODE_ENV === 'development') {
  alert('请配置 API_ROOT, CSRF, 路径:config/dev.env.js')
}
axios.defaults.baseURL = process.env.API_ROOT;
axios.defaults.headers.post['Content-Type'] = 'application/x-www-fromurlencodeed';
axios.defaults.withCredentials = true;
axios.interceptors.response.use(
  response => {
    return response;
  },
  error => {
    if (error.response) {
      console.error(error.response);
      switch (error.response.status) {
        case 401:
          // 返回 401 验证错误
          console.log(error.response.data.url);

          document.location = error.response.data.url
      }
    }
    return Promise.reject(error.response.data)
  }
);
export default axios
