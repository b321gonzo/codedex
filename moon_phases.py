def moon_phase(phase):
  Phases = ['New Moon','Waxing Crescent','First Quarter','Waxing Gibbous','Full Moon','Waning Gibbous','Last Quarter','Waning Crescent']
  phase_image = ['🌑','🌒','🌓','🌔','🌕','🌖','🌗','🌘']
  return(phase_image[Phases.index(phase)])

answer = moon_phase("New Moon")
print(answer)