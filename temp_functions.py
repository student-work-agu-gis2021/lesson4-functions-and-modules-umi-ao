def fahr_to_celsius(temp_fahrenheit):
  return (temp_fahrenheit-32)/1.8

def temp_classifier(temp_celsius):
  ##Temperatures below -2 degrees Celsius  
  if(temp_celsius<-2):
    return 0
  ##Temperatures equal or warmer than -2, but less than +2 degrees Celsius 
  elif(temp_celsius>=-2)and(temp_celsius<2):
    return 1
  ##Temperatures equal or warmer than +2, but less than +15 degrees Celsius 
  elif(temp_celsius>=2)and(temp_celsius<15):
    return 2
  ##Temperatures equal or warmer than +15 degrees Celsius          
  elif(temp_celsius>=15):
    return 3