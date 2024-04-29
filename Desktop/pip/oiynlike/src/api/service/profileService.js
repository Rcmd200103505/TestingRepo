import HttpRequests from "@/api/httpRequests";

export default class ProfileService {
  static fetchProfile() {
    return HttpRequests.get("/api/user/profile");
  }

  static updateProfile(data) {
    return HttpRequests.patch("/api/user/profile", data);
  }

  static uploadImage(formData) {
    return HttpRequests.post("/api/user/profile", formData, null, {
      headers: {
        "Content-Type": "multipart/form-data",
      },
    });
  }
}
