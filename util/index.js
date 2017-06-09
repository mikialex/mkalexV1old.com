var http = require('https');
var cheerio = require('cheerio');

var url = 'https://www.behance.net/gallery/53248723/SUOL-2017';

http.get(url, function(response) {

    var body = '';

    response.on('data', function(d) {
      body += d;
    });
    //
    response.on('end', function() {
    //   var parsed = JSON.parse(body);
    //   callback({
    //     email: parsed.email,
    //     password: parsed.pass
    //   });

    var text= '<img src=https://mir-s3-cdn-cf.behance.net/project_modules/1400/32efce53248723.592db8cc7c28f.jpg>'
    var $ = cheerio.load(body, {decodeEntities: false});
    images=$('img').attr('src')
    console.log(images)

    // images.forEach(function(img){
    //     console.log(img)
    // })
    });

  });
