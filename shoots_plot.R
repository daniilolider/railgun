library (readr)

# Читаем файл.
data <- read_csv("shoots.csv")

# Выводим график.
plot(data$x,
     data$y,
     main="100 random shoots",
     xlab="Coord x",
     ylab="Corrd y",
     pch=13)  # Пусть будут кружочки с крестиками.
