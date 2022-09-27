# Personal Programming Project

## Sudarsan Manjunatha Pai

### Matrkl no : 65109


$$x_{1,2} = \frac{-b \pm \sqrt{b^2-4ac}}{2b}.$$

$R_a = \frac{1}{l_e} = \int_0^{l_e} \left\| z(x) \right\| dx$









$\text{Latex}$ | Feature Name | Description
--- | --- | ---
$R_a = \frac{1}{l_e} = \int_0^{l_e} \left\| z(x) \right\| dx$ | r_a | Oberflächentextur Profil [ISO 21920-2]. The arithmetic mean height parameter $R_a$ is the arithmetic mean of the absolute values of the ordinate values. $l_e$ is the evaluation length.
$R_{z} = \frac{1}{N} \sum_{i=1}^N \underset{j \in N_{p,i}}{max}(Z_{ph,j} + \underset{k \in N_{v,i}}{max}(Z_{vd,k}))$ | r_z | The maximum height parameter $R_z$ is the mean value, from all section lengths, of the per section sum of the largest peak height and largest pit depth.
$S_a = \frac{1}{A} \iint_{\tilde{A}} \left\| z(x,y) \right\| dxdy$ | s_a | Oberflächentextur Fläche [ISO 25178-2]. $\tilde{A}$ ist die domain (Mathematische abbildung) der Fläche.  The arithmetic mean height parameter $S_a$ is the mean of the absolute values of the scale limited surface.
$S_q = \sqrt{\frac{1}{A} \iint_{\tilde{A}} \left\| z^2(x,y) \right\| dxdy}$ | s_q | The RMS $S_q$ is the mean of the absolute values of the scale limited surface.
$V_{VV} = V_V(p) = \frac{K}{100\%} \int_{p}^{100\%} S_{mc}(p) - S_{mc}(q) dq$ | v_ges | Dale Void Volume.


### Zugversuche
$\text{Latex}$ | Feature Name | Description
--- | --- | ---
$m_e$ | m_e | Steigung im linearelastischen bereich
$r_{p02}$ | r_p02 | Dehngrenze
$r_m$ | r_m | Tensile strenght (Zugfestigkeit)
$a_{50}$ | a_50 | Bruchdehnung

### Material Properties (**Preliminary**)
erw = erwärmen & abk = abkühlen. abk is considered irrelevant since timeframe is extended.

$\text{Latex}$ | Feature Name | Unit | Description
--- | --- | --- | ---
$R_c$ | r0_temp / r5_temp / r15_temp / r30_temp  | $\mu \Omega$ |  Contact resistance
$\rho_e$ | erw_elektr_wider_temp | $\Omega mm^2/m$ | Specific electrical resistance. First value of temperature range
$\sigma_e$ | erw_elektr_leitf_temp | $m/\Omega mm^2$ | Electric conductivity (calculated)
$\lambda_T$ | erw_temp_leitf_temp | $W/mK$ | Thermal conductivity (calculated)
$\text{None}$ | erw_waerme_leitf_temp | $mm^2/s$ | Heat conductivity (calculated)
$C_p$ | waermekapa_20 | $J / kgK$ | Heat capacity. p=const. pressure
$\alpha_T$ | erw_waremeausdehnung_temp | $10^{-6}/K$ | Thermal expansion coefficient

