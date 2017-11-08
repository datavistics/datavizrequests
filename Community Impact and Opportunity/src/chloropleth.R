library(choroplethr)
library(choroplethrZip)

df <- read.csv("..\\data\\ci_and_op_data.csv")
community_score <- df[c(7,5)]
names(community_score) <- c('region', 'value')
community_score$region <- as.character(community_score$region)
zip_choropleth(community_score,
               state_zoom = "pennsylvania",
               title = "Pennsylvania Community score per zip code",
               legend = "Community score")

opportunity_score <- df[c(7,6)]
names(opportunity_score) <- c('region', 'value')
opportunity_score$region <- as.character(opportunity_score$region)
zip_choropleth(opportunity_score,
               state_zoom = "pennsylvania",
               title = "Pennsylvania Opportunity score per zip code",
               legend = "Opportunity score")

composite_col <- df$normalized_community_score + df$OPPORTUNITY.SCORE
composite_score <- data.frame(df$ZIP.CODE, composite_col)
names(composite_score) <- c('region', 'value')
composite_score$region <- as.character(composite_score$region)
zip_choropleth(composite_score,
               state_zoom = "pennsylvania",
               title = "Pennsylvania Composite score per zip code",
               legend = "Composite score")
