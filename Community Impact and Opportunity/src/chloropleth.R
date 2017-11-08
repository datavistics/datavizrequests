library(choroplethr)
library(choroplethrZip)

df <- read.csv("..\\data\\ci_and_op_data.csv")
community_score <- df[c(7,5)]
names(community_score) <- c('region', 'value')
community_score$region <- as.character(community_score$region)
zip_choropleth(community_score,
               state_zoom = "pennsylvania",
               title = "Pennsylvania Community Impact score per zip code",
               legend = "Community Impact score")

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

senior_pop <- read.csv("..\\data\\other_data.csv")
senior_pop$Senior.Occupancy..SO. <- as.numeric(sub("%","",senior_pop$Senior.Occupancy..SO.))/100
senior_pop$Senior.Rent.Burden..SRB. <- as.numeric(sub("%","",senior_pop$Senior.Rent.Burden..SRB.))/100
senior_pop$Senior.Housing.Stock..SHS. <- as.numeric(sub("%","",senior_pop$Senior.Housing.Stock..SHS.))/100
senior_pop$Zip.Code <- as.character(senior_pop$Zip.Code)

occupancy <- senior_pop[c(1,2)]
names(occupancy) <- c('region', 'value')
occupancy$region <- as.character(occupancy$region)
zip_choropleth(occupancy,
               state_zoom = "pennsylvania",
               title = "Pennsylvania Senior Occupancy per zip code",
               legend = "Occupancy Percentage")

rent_burden <- senior_pop[c(1,2)]
names(rent_burden) <- c('region', 'value')
rent_burden$region <- as.character(rent_burden$region)
zip_choropleth(rent_burden,
               state_zoom = "pennsylvania",
               title = "Pennsylvania Senior Rent Burden per zip code",
               legend = "Rent Burden Percentage")

housing_stock <- senior_pop[c(1,2)]
names(housing_stock) <- c('region', 'value')
housing_stock$region <- as.character(housing_stock$region)
zip_choropleth(housing_stock,
               state_zoom = "pennsylvania",
               title = "Pennsylvania Senior Housing Stock per zip code",
               legend = "Housing Stock Percentage")
