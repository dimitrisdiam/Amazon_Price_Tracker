# Amazon_Price_Tracker
<img width="622" alt="Screenshot 2022-05-02 at 6 04 06 PM" src="https://user-images.githubusercontent.com/64299794/166257877-24c3e743-7952-4c6f-8451-30eba54fb416.png">

The picture displays the email which informs us about the updated price of the product.

## Data Extraction Tools
Beautiful Soup

## Programming Languages
Python

## Project description
The project had as purpose the observation of a specific product's price in order to send us an email when the price will be equal or lower than the desired.

## Solution

Firstly, I had to get access to Amazon's data and clean them with BeautifulSoup. After that, I found the headers which were necessary to read Amazon's page. So, I scraped the product's price which we wanted and I created an algorithm that would send me an email when the product's price was dropped down to the desired. Finally, we repeated the algorithm once a day until the day which the email was sent to me and I bought the product.
