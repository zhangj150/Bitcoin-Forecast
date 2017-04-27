# Made file “ALL_dates_from_earliest.csv” using Excel to calculate days since earliest date (Jan 6, 2015).  Same day would be 0 days away, next day would be 1 day way, etc. Columns of this file are dates, mentions, and distance.

# Tutorial for this R package:
# https://cran.r-project.org/web/packages/Ckmeans.1d.dp/vignettes/Ckmeans.1d.dp.html

# CRAN site:
# https://cran.r-project.org/web/packages/Ckmeans.1d.dp/ 

# New file ALL_clusters.csv has additional column, res.cluster ranging from 1 to 27 (the cluster to which the data point belongs to)

require(Ckmeans.1d.dp)

data_file = read.csv("ALL_dates_from_earliest.csv")

dates = data_file$date
occurrences = data_file$occurrences
distance = data_file$distance

res = Ckmeans.1d.dp(distance, k = c(1:28),occurrences)

write.csv(data.frame(dates, distance, occurrences, res$cluster), "ALL_clusters.csv", quote = FALSE, row.names = FALSE)

plot(distance, occurrences,col=res$cluster,pch=res$cluster,type="h", xlab="Time (Days)", ylab="Mentions")