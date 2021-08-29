setwd("/Users/rctrj/Downloads/LeetCode")


install.packages("readxl")
library("readxl")


movie_data <- read_excel("ICC Test Bat 3001.xlsx")

cricket_data <- as.data.frame(movie_data)

head(cricket_data)


data <- cricket_data[!is.na(cricket_data$Avg) &
                       cricket_data$Runs > 2000,]
data <- data[order(-data$Avg),]
data <- head(data, 20)

data

pt <- ggplot(data = data, 
             aes(x = Player, y = Avg)) +
              geom_bar(stat = "identity", 
                       fill = "Blue", color = "Red") +
  theme(axis.text.x = element_text(angle = 90, vjust = 0.5, hjust=1))

pt



season_data <- read.csv("Season_data.csv")
head(season_data)


pt <- ggplot(data = season_data) +
  geom_bar(stat = "identity", aes(x = Year, y = Runs...Innings)
           , fill = "Blue", color = "Red", size = 0.5) +
  geom_smooth(aes(x = Year, y = Runs...Innings), fill = NA) +
  ylab("Runs per Innings")

pt


head(cricket_data[!is.na(cricket_data$Runs),], 20)

library(dplyr)
install.packages("tidyr")
library(tidyr)
library(stringr)


?separate


cricket_data %>% separate(cricket_data, cricket_data$Player, c("Player", "Country"), sep = " \\(", remove=F)

str_split_fixed(cricket_data$Player, "\\(", 2)

head(cricket_data)
## removing the NAs

??dcast


lbw_data <- read.csv("LBW.csv")


head(lbw_data)


lbw_data$X..LBW.Dismissals <- as.numeric(gsub("\\%", "", lbw_data$X..LBW.Dismissals))

ptt <- ggplot(data = lbw_data) +
  geom_bar(stat = "identity", aes(x = Year, y = X..LBW.Dismissals)
           , fill = "Blue", color = "Red", size = 0.5) +
  geom_smooth(aes(x = Year, y = X..LBW.Dismissals), fill = NA) +
  xlab("Year") +
  ylab("Percentage of LBW decisions")

ptt


host_data <- read.csv("host_country.csv")


head(host_data)

ptt <- ggplot(data = host_data) +
  geom_bar(stat = "identity", aes(x = Host.Country, y = Ave)
           , fill = "Blue", color = "Red", size = 0.5) +
  geom_smooth(aes(x = Host.Country, y = Ave), fill = NA) +
  xlab("Host Country") +
  ylab("Averages") +
  theme(axis.text.x = element_text(angle = 90, vjust = 0.5, hjust=1))

ptt
