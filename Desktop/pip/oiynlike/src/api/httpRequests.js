import axiosInstance from "./axiosInstance";

class HttpRequests {
  static async request(method, url, data = null, params = null, options = {}) {
    const response = await axiosInstance({
      method,
      url,
      data,
      params,
      ...options,
    });

    return response.data;
  }

  static get(url, params = null, options = {}) {
    return this.request("get", url, null, params, options);
  }

  static post(url, data = null, params = null, options = {}) {
    return this.request("post", url, data, params, options);
  }

  static patch(url, data = null, params = null, options = {}) {
    return this.request("patch", url, data, params, options);
  }

  static put(url, data = null, params = null, options = {}) {
    return this.request("put", url, data, params, options);
  }

  static delete(url, params = null, options = {}) {
    return this.request("delete", url, null, params, options);
  }
}

export default HttpRequests;
