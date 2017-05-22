close all; clear all;

freqs = [40.7, 40.7, 40.0, 39.4]; % kHz - bestemt ned til +/- 1 Hz
startPoints = [15.7, 15.4, 15.2, 15.3]; % cm punkt
endPoints = [28.6, 26.5, 28.2, 26.9]; % cm punkt
numberWavelengths = [15, 13, 15, 13]; % antal
% Usikerhed er 0.1 cm 

wavelengths = (endPoints - startPoints) ./ numberWavelengths ; % i cm - finder bølgelængder 
sigmaWavelengths = 0.1 ./ numberWavelengths ; % Da fejlen er på +/- 0.1 cm

temperatur = 22.0 ; % i Celsius +/- 0.1
speedOfSound = 331.3 * sqrt(1 + ( temperatur / 273.15 ) ) ; % fra wikipedia
theoreticalValues = (speedOfSound * 100) ./ ((39:0.1:41) * 1000) ; % vha. lambda = v /f

% Ved plot ses at nedenstående er negligible
sigmatheoreticalValues1 = (331.3 * sqrt(1 + ( (temperatur + 0.1)/ 273.15 ) ) * 100) ./ ((39:0.1:41) * 1000);
sigmatheoreticalValues2 = (331.3 * sqrt(1 + ( (temperatur - 0.1)/ 273.15 ) ) * 100) ./ ((39:0.1:41) * 1000);

ft = fittype('a / x', 'Independent', 'x');
f = fit(freqs', wavelengths', ft);


figure 
hold on
errorbar(freqs, wavelengths, sigmaWavelengths, 'ob')
plot(39:0.1:41, theoreticalValues, '--r')
plot(f, '--k')
xlim([39 41])
ylim([0.845 0.9])
xlabel('$f$ [kHz]', 'Interpreter', 'Latex', 'FontSize', 20)
ylabel('$\lambda$ [cm]', 'Interpreter', 'Latex', 'FontSize', 20)
l = legend('Data', 'Teori ($\lambda = \frac{34.4}{f}$)', 'Fit ($\lambda = \frac{34.9}{f}$)');
set(l, 'Interpreter', 'Latex', 'FontSize', 16)
hold off