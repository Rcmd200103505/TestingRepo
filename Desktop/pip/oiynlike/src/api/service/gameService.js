import HttpRequests from "@/api/httpRequests";

export default class GameService {
  static fetchRecommendedGamecards() {
    return HttpRequests.get("/api/gamecards");
  }

  static fetchUserGamecards() {
    return HttpRequests.get("/api/user/gamecards");
  }

  static createGame(data) {
    return HttpRequests.post("/api/gamecards", data);
  }

  static joinGame(gameCardId) {
    return HttpRequests.put("/api/join", { gameCardId });
  }
}
