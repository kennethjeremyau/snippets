d = new Date("2017-01-01");
console.log(d);
d = new Date("2017-01-01T01:00:00");
console.log(d);
// Removing the 'T' makes it local time.
d = new Date("2017-01-01 01:00:00");
console.log(d);
d = new Date("2017-01-01T01:00:00-07:00");
console.log(d);
