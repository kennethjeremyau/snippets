function printDate(d) {
    var year = d.getFullYear();
    var month = d.getMonth() + 1;
    var day = d.getDate();
    var hours = d.getHours();
    var minutes = d.getMinutes();
    var seconds = d.getSeconds();
    return year + '-' +
        (month < 10 ? '0': '') + month + "-" +
        (day < 10 ? '0': '') + day + " " +
        (hours < 10 ? '0': '') + hours + ":" +
        (minutes < 10 ? '0': '') + minutes + ":" +
        (seconds < 10 ? '0': '') + seconds;
}

var d = new Date();
console.log(printDate(d));
