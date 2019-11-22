let d = new Date("2017-01-01");
console.log(d);

d = new Date("2017-01-01 01:00:00");
console.log(d);

// ISO 8601
d = new Date("2017-01-01T01:00:00");
console.log(d);

d = new Date("2017-01-01T01:00:00-07:00");
console.log(d);

d = new Date("2017", "1" - 1, "1");
console.log(d);

d = new Date(2017, 0, 1);
console.log(d);

d = new Date (2017, 0, -5);
console.log(d);
