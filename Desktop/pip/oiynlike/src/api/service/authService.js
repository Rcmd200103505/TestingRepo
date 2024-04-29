import HttpRequests from "@/api/httpRequests";

export default class AuthService {
  static login(data) {
    return HttpRequests.post("api/users/login", data);
  }

  static register(data) {
    return HttpRequests.post("api/users/signup", data);
  }
}
