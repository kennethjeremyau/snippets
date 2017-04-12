var regex = /^(\d+)-(\d+)-(\d+)$/;
var string = "2017-04-12";
var match = regex.exec(string);
for (var i = 1; i < match.length; i++) {
    console.log(match[i]);
}
