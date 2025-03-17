def kreis_umfang(r):
  pi=3.14
  return(2*pi*r)
  
  def kreis_flaeche(r):
    pi=3.14
    print("flaeche=" + str(pi*r*r))
    
    def zylinder_volumen(r,h):
      pi=3.14
      print("Flaeche=" + str(pi*r*r*h))
      
      print("Was würden sie machen ? bitte eingeben")
      f=int(input("1 für Umfang 2 für Flaeche 3 für Volumen")),
      if f==1:
        r=int(input("Radius:"))
        test.kreis_umfang(r)
  