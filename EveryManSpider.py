import scrapy

class CinemaSpider(scrapy.Spider):
    name = "movieSpider"
    allowed_domains = ['everymancinema.com']
    start_urls = [
        'https://www.everymancinema.com/kings-cross/film-listings'
    ]

    def parse(self, response):
        moviesContainer = response.css("ul.gridRow.films-1") 
        for movie in moviesContainer:
            # movie data located at li.gridRow.filmItem --> HTML location of the data
            for movie_data in movie.css('div.clearfix'):
                descData = movie_data.css('div.gridCol-s-12.gridCol-m-5.gridCol-l-5.p_rel')
                screening = movie.css('ul.filmTimes')
                    
                if descData.css("h2.filmItemTitle a::text").extract():

                    yield{

                        descData.css("h2.filmItemTitle a::text").extract()[0] : {
                            'screening' : screening.css('a::text').extract()
                        }

                    }
                       
               





