# IVDR Visualizer
This project use an arduino-based IVDR (In Vehicle Data Recoder) to obtain data from an OBD2 port. The python script takes the data entrying from the Serial port in the computer
sent by the IVDR, treats it and plot live data in real time. This project was created with the aim of automate the manual process of applying specific formulas to each message of
OBD2 and create easy to read graph in real time of the data arriving from the car.

Currently, it is configured to show RPM in real time. It also provides a graph of the ERF (Engine Fuel Rate) obatined directly by the sensor versus the EFR value obtained by using
the Mass air flow sensor (MAF) air flow rate and the fule-air ratio. Finally, by using both EFR values, it provides a graph of the real time fuel consumption of the car.
