export default class DateUtil {
  static isValidDate(date) {
    const parsedDate = new Date(date);

    return parsedDate instanceof Date && !isNaN(date);
  }

  static formatDate(date, options = { displayTime: true, displayYear: false }) {
    const months = [
      "Января",
      "Февраля",
      "Марта",
      "Апреля",
      "Мая",
      "Июня",
      "Июля",
      "Августа",
      "Сентября",
      "Октября",
      "Ноября",
      "Декабря",
    ];

    const parsedDate = new Date(date);

    const day = parsedDate.getDate();
    const month = months[parsedDate.getMonth()];
    const year = parsedDate.getYear();
    const hours = String(parsedDate.getHours()).padStart(2, "0");
    const minutes = String(parsedDate.getMinutes()).padStart(2, "0");

    let result = `${day} ${month}`;

    if (options.displayYear) {
      result += ` ${year}`;
    }

    if (options.displayTime) {
      result += `, ${hours}:${minutes}`;
    }

    return result;
  }
}
