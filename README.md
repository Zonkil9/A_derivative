# A_derivative
This is a Python code for calculating the first derivative of the **A<sub>*iso*</sub>** tensor (Fermi contact interaction). This quantity is also known as the Bloembergen effect constant *a<sub>i</sub><sup>(1)</sup>*. It was used in [Pluta, T.; Skrzyński, G. J. Phys. Chem. A 128, 8080-8087, 2024](https://doi.org/10.1021/acs.jpca.4c04480).

The Bloembergen effect constant is further explained in, e.g., [Karna S.P. J. Comput. Chem. 20: 1274–1280, 1999](https://doi.org/10.1002/(SICI)1096-987X(199909)20:12<1274::AID-JCC7>3.0.CO;2-7).

## Preparations
Firstly, one needs to calculate the **A<sub>*iso*</sub>** tensors for the desired molecule with external electric fields using [Orca software](https://orcaforum.kofo.mpg.de) (tested on the 5.0.4 version). These are finite field calculations. Input example:
```sh
# Geo from RJB jcp 156(2022)094107                                                                                                                                                                                 

! UKS CAM-B3LYP aug-cc-pVTZ-J AutoAux VeryTightSCF NoFrozenCore

%MaxCore 6000

% pal  nprocs  4
end

%output
  Print[ P_Hirshfeld ] 1
end

%scf
   EField  0.0005, 0.0, 0.0
end

* xyz  0 3
 C                    -5.234025       2.1482889     -0.023721
 H                    -6.224911       2.1482889      0.4001037
 H                    -4.2431396      2.1482889      0.4001037
*

%eprnmr
Nuclei = all C{aiso,rho};
Nuclei = all H{aiso,rho};
end
```


## How to use
Execute the command and provide proper information:
```sh
python A_derivative.py
```

The program takes the Orca outputs as input.
