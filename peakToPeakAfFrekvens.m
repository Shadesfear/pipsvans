close all; clear all;

data = dataset('File', 'PeaktopeakAfFrekvens.csv', 'Delimiter', ',');

figure
hold on
plot(data.Frekvens_kHz_, data.PeakToPeak_V_, 'o')
xlabel('Frekevsn [kHz]')
ylabel('Peak to Peak [V]')
hold off