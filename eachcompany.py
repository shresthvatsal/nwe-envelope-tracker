import yfinance as yf

def is_bullish(stock_data, index):
    # Check if the stock is in a bullish pattern
    # You can customize this logic based on your specific criteria
    return stock_data['Close'].iloc[index] > stock_data['Open'].iloc[index]

def calculate_return(stock_symbol):
    # Fetch historical stock price data


    stock_data = yf.download(stock_symbol, start="2023-01-01", end="2023-11-01")

    # Check if stock_data is empty
    if stock_data.empty:
        pass
    else:
        pass

    # Initialize variables
    initial_cash = 100000  # Initial investment amount
    cash = initial_cash
    shares = 0
    stop_loss_percentage = 0.10  # 10% stop loss
    sell_price = 0  # Initialize sell_price

    # Loop through the entire stock data
    for i in range(3, len(stock_data)):
        # Check if the stock is in a bullish pattern
        if not is_bullish(stock_data, i):
            continue  # Skip trading if not in a bullish pattern

        # Calculate the sum of % change for Monday, Tuesday, and Wednesday
        cumulative_percentage_change = (
            (stock_data['Close'].iloc[i-3] - stock_data['Open'].iloc[i-3]) / stock_data['Open'].iloc[i-3] +
            (stock_data['Close'].iloc[i-2] - stock_data['Open'].iloc[i-2]) / stock_data['Open'].iloc[i-2] +
            (stock_data['Close'].iloc[i-1] - stock_data['Open'].iloc[i-1]) / stock_data['Open'].iloc[i-1]
        )

        # Check if the cumulative change is negative (bearish)
        if cumulative_percentage_change < 0:
            # Buy on the fourth day if the stock is bearish
            buy_price = stock_data['Open'].iloc[i]

            # Check if sell_price is not already assigned
            if sell_price == 0:
                # Sell on the very first day it gives a red candle
                if stock_data['Close'].iloc[i] < stock_data['Open'].iloc[i]:
                    sell_price = stock_data['Close'].iloc[i]
                # Sell if the stock touches the stop loss
                elif stock_data['Low'].iloc[i] < buy_price * (1 - stop_loss_percentage):
                    sell_price = buy_price * (1 - stop_loss_percentage)
                # Sell on the next Monday
                else:
                    next_monday_index = i + (7 - i % 7)
                    sell_price = stock_data['Open'].iloc[next_monday_index]

                # Update cash and shares
                shares = cash / buy_price
                cash = 0
                break

    # Calculate the return
    final_value = cash + shares * sell_price
    return_percentage = ((final_value - initial_cash) / initial_cash) * 100

    return return_percentage

# List of stocks
stocks = ['ET.NS', 'NPS.NS', 'PM.NS', 'AAA.NS', 'ABB.NS', 'ABB.NS', 'ABM.NS', 'ACC.NS', 'ACC.NS', 'ADF.NS', 'AGI.NS', 'AGI.NS', 'AGS.NS', 'AIA.NS', 'AJR.NS', 'AKG.NS', 'AKG.NS', 'AMD.NS', 'AMJ.NS', 'APL.NS', 'ARSS.NS', 'ART.NS', 'ASK.NS', 'AVG.NS', 'AVG.NS', 'AVT.NS', 'AYM.NS', 'AARON.NS', 'AARVI.NS', 'AAVAS.NS', 'ABAN.NS', 'AHL.NS', 'ACE.NS', 'ATGL.NS', 'AWL.NS', 'ABFRL.NS', 'AMC.NS', 'AFFLE.NS', 'ATFL.NS', 'AIRAN.NS', 'AKASH.NS', 'AKI.NS', 'ALKEM.NS', 'ATL.NS', 'ADSL.NS', 'ALPA.NS', 'M.NS', 'AMBER.NS', 'ACL.NS', 'APCL.NS', 'ANMOL.NS', 'AWHCL.NS', 'APEX.NS', 'APTUS.NS', 'ACI.NS', 'ADL.NS', 'ARIES.NS', 'ARVEE.NS', 'ASTEC.NS', 'DM.NS', 'ATAM.NS', 'ATUL.NS', 'AURUM.NS', 'ASAL.NS', 'DMART.NS', 'AXITA.NS', 'B.NS', 'C.NS', 'BCP.NS', 'B.NS', 'L.NS', 'B.NS', 'B.NS', 'BBTCL.NS', 'BAG.NS', 'BASF.NS', 'BASF.NS', 'BCL.NS', 'BEML.NS', 'BLAL.NS', 'BEML.NS', 'BEML.NS', 'BF.NS', 'BF.NS', 'BGR.NS', 'BKM.NS', 'BLB.NS', 'BLS.NS', 'BLS.NS', 'BPL.NS', 'BPL.NS', 'BSE.NS', 'BSE.NS', 'BSL.NS', 'BSL.NS', 'BAJAJ.NS', 'AUTO.NS', 'BANG.NS', 'BANKA.NS', 'BASML.NS', 'BVCL.NS', 'ASMS.NS', 'BEPL.NS', 'BBL.NS', 'BDL.NS', 'BEL.NS', 'BHEL.NS', 'BPCL.NS', 'BRNL.NS', 'BIL.NS', 'BSOFT.NS', 'BBOX.NS', 'GVS.NS', 'BTML.NS', 'BBTC.NS', 'BRFL.NS', 'BSHSL.NS', 'BCG.NS', 'C.NS', 'C.NS', 'CANDC.NS', 'C.NS', 'E.NS', 'CARE.NS', 'CCL.NS', 'CCL.NS', 'CESC.NS', 'CESC.NS', 'CG.NS', 'CIE.NS', 'CL.NS', 'CLC.NS', 'CMI.NS', 'CMS.NS', 'CSB.NS', 'CSL.NS', 'CTE.NS', 'CANBK.NS', 'CGCL.NS', 'E.NS', 'CELLO.NS', 'CDSL.NS', 'CERA.NS', 'CLSEL.NS', 'CIPLA.NS', 'CUB.NS', 'CLEAN.NS', 'CAMS.NS', 'CCCL.NS', 'CCHHL.NS', 'COX.NS', 'KINGS.NS', 'CREST.NS', 'CROWN.NS', 'CUPID.NS', 'DLM.NS', 'D.NS', 'B.NS', 'D.NS', 'P.NS', 'D.NS', 'P.NS', 'D.NS', 'DB.NS', 'DB.NS', 'DC.NS', 'DCI.NS', 'DCB.NS', 'DCM.NS', 'DCM.NS', 'DCM.NS', 'DCM.NS', 'DCM.NS', 'DCM.NS', 'DCW.NS', 'DCW.NS', 'DCX.NS', 'DFM.NS', 'DIC.NS', 'DJ.NS', 'DJML.NS', 'DLF.NS', 'DLF.NS', 'DMCC.NS', 'DMCC.NS', 'DRC.NS', 'DSJ.NS', 'DABUR.NS', 'DIL.NS', 'DEN.NS', 'DEVIT.NS', 'DBOL.NS', 'DHANI.NS', 'DHRUV.NS', 'DTIL.NS', 'DVL.NS', 'DBL.NS', 'TV.NS', 'DCAL.NS', 'DIXON.NS', 'DODLA.NS', 'DUCON.NS', 'DSSL.NS', 'DYCL.NS', 'EID.NS', 'EIH.NS', 'EIH.NS', 'EMS.NS', 'EPL.NS', 'EPL.NS', 'ESAF.NS', 'EMIL.NS', 'ELIN.NS', 'EMCO.NS', 'EMKAY.NS', 'EMMBI.NS', 'ENIL.NS', 'ERIS.NS', 'ESTER.NS', 'EIFFL.NS', 'EKC.NS', 'FCS.NS', 'FDC.NS', 'FDC.NS', 'FIEM.NS', 'FSN.NS', 'E.NS', 'NYKAA.NS', 'E.NS', 'FCL.NS', 'FSL.NS', 'FOCUS.NS', 'FEL.NS', 'FLFL.NS', 'FMNL.NS', 'FSC.NS', 'G.NS', 'M.NS', 'G.NS', 'R.NS', 'G.NS', 'GACM.NS', 'GAIL.NS', 'GAIL.NS', 'GE.NS', 'GEPIL.NS', 'GE.NS', 'T.NS', 'D.NS', 'GET.NS', 'D.NS', 'GFL.NS', 'GHCL.NS', 'GHCL.NS', 'GHCL.NS', 'GI.NS', 'TPHQ.NS', 'GIC.NS', 'GKW.NS', 'GMM.NS', 'GMR.NS', 'GMR.NS', 'GMRP.NS', 'UI.NS', 'GNA.NS', 'GNA.NS', 'GOCL.NS', 'GP.NS', 'GPT.NS', 'GRM.NS', 'GRP.NS', 'GSS.NS', 'GSS.NS', 'GTL.NS', 'GTL.NS', 'GTL.NS', 'GTN.NS', 'GTPL.NS', 'GTPL.NS', 'GVK.NS', 'GVP.NS', 'GRSE.NS', 'GDL.NS', 'GATI.NS', 'GICRE.NS', 'GLAND.NS', 'GLAXO.NS', 'GLS.NS', 'GSLSU.NS', 'GLOBE.NS', 'GPIL.NS', 'GODHA.NS', 'GOKEX.NS', 'GOKUL.NS', 'GAEL.NS', 'GIPCL.NS', 'GLFL.NS', 'GNFC.NS', 'GPPL.NS', 'GSFC.NS', 'GSPL.NS', 'HB.NS', 'HBSL.NS', 'HBL.NS', 'HCL.NS', 'HCL.NS', 'INSYS.NS', 'HCL.NS', 'HDFC.NS', 'HDFC.NS', 'HDFC.NS', 'HEC.NS', 'HEG.NS', 'HEG.NS', 'HFCL.NS', 'HFCL.NS', 'HG.NS', 'HIL.NS', 'HIL.NS', 'HLE.NS', 'HLV.NS', 'HMA.NS', 'HMT.NS', 'HMT.NS', 'HOV.NS', 'HOVS.NS', 'HP.NS', 'HPAL.NS', 'HPL.NS', 'HPL.NS', 'HT.NS', 'UP.NS', 'HCG.NS', 'HIKAL.NS', 'HSCL.NS', 'HPIL.NS', 'HGS.NS', 'HAL.NS', 'HCC.NS', 'HMVL.NS', 'HDIL.NS', 'HDFC.NS', 'HUDCO.NS', 'I.NS', 'G.NS', 'IGPL.NS', 'ICDS.NS', 'ICE.NS', 'ICICI.NS', 'ICICI.NS', 'ICICI.NS', 'ICICI.NS', 'ISEC.NS', 'ICRA.NS', 'ICRA.NS', 'IDBI.NS', 'IDBI.NS', 'IDFC.NS', 'IDFC.NS', 'IDFC.NS', 'IFB.NS', 'IFB.NS', 'IFCI.NS', 'IFCI.NS', 'IFGL.NS', 'IIFL.NS', 'IIFL.NS', 'IIFL.NS', 'IKIO.NS', 'IKIO.NS', 'IL.NS', 'FS.NS', 'IL.NS', 'IL.NS', 'FS.NS', 'IVC.NS', 'IL.NS', 'FS.NS', 'IL.NS', 'IMP.NS', 'IOL.NS', 'IOLCP.NS', 'IRB.NS', 'IRB.NS', 'IRIS.NS', 'IRIS.NS', 'IRIS.NS', 'IRM.NS', 'ISGEC.NS', 'ISGEC.NS', 'ISMT.NS', 'ITC.NS', 'ITC.NS', 'ITD.NS', 'ITI.NS', 'ITI.NS', 'IVP.NS', 'IVP.NS', 'IZMO.NS', 'IZMO.NS', 'IMPAL.NS', 'IPL.NS', 'ITDC.NS', 'E.NS', 'IEL.NS', 'IEX.NS', 'IMFA.NS', 'IOC.NS', 'IOB.NS', 'IRCTC.NS', 'IRFC.NS', 'ICIL.NS', 'IGL.NS', 'IITL.NS', 'INFY.NS', 'IWEL.NS', 'ISFT.NS', 'E.NS', 'IEX.NS', 'IMFA.NS', 'IOC.NS', 'IOB.NS', 'IRCTC.NS', 'IRFC.NS', 'ICIL.NS', 'IGL.NS', 'IITL.NS', 'INFY.NS', 'IWEL.NS', 'ISFT.NS', 'E.NS', 'JOCIL.NS', 'JCHAC.NS', 'JMA.NS', 'JLHL.NS', 'JWL.NS', 'E.NS', 'KBC.NS', 'KCP.NS', 'KCP.NS', 'KCP.NS', 'KDDL.NS', 'KDDL.NS', 'KEC.NS', 'KEC.NS', 'KEI.NS', 'KEI.NS', 'KFIN.NS', 'KIOCL.NS', 'KIOCL.NS', 'KM.NS', 'KNR.NS', 'KPI.NS', 'KPIT.NS', 'KPR.NS', 'KRBL.NS', 'KRBL.NS', 'KSB.NS', 'KSB.NS', 'KPIL.NS', 'KICL.NS', 'KSL.NS', 'KSCL.NS', 'KAYA.NS', 'KKCL.NS', 'I.NS', 'KECL.NS', 'KITEX.NS', 'KOVAI.NS', 'KIMS.NS', 'KRITI.NS', 'L.NS', 'T.NS', 'L.NS', 'TFH.NS', 'L.NS', 'T.NS', 'LTTS.NS', 'LCC.NS', 'LG.NS', 'LGB.NS', 'LIC.NS', 'LT.NS', 'LTIM.NS', 'RG.NS', 'LFIC.NS', 'LPDC.NS', 'LT.NS', 'LASA.NS', 'LEXUS.NS', 'LIBAS.NS', 'LICI.NS', 'LINC.NS', 'LAL.NS', 'LUPIN.NS', 'M.NS', 'K.NS', 'MKPL.NS', 'M.NS', 'M.NS', 'MMFL.NS', 'MBL.NS', 'MEP.NS', 'MEP.NS', 'MIC.NS', 'MICEL.NS', 'MIRC.NS', 'MMP.NS', 'MMP.NS', 'MMTC.NS', 'MMTC.NS', 'MOIL.NS', 'MOIL.NS', 'MPS.NS', 'MPS.NS', 'MRF.NS', 'MRF.NS', 'MRO.NS', 'TEK.NS', 'MRO.NS', 'TEK.NS', 'MSP.NS', 'MSPL.NS', 'MSTC.NS', 'MT.NS', 'MTAR.NS', 'CNC.NS', 'LODHA.NS', 'MCL.NS', 'MBAPL.NS', 'MGL.NS', 'MTNL.NS', 'M.NS', 'MFIN.NS', 'M.NS', 'M.NS', 'EPC.NS', 'MHRIL.NS', 'MGEL.NS', 'MRPL.NS', 'N.NS', 'MVGJL.NS', 'MFSL.NS', 'MAZDA.NS', 'MBECL.NS', 'MOKSH.NS', 'MSUMI.NS', 'MUFIN.NS', 'MCX.NS', 'N.NS', 'K.NS', 'NKIND.NS', 'N.NS', 'R.NS', 'NRAIL.NS', 'NACL.NS', 'NAVA.NS', 'NAVA.NS', 'NBCC.NS', 'NBCC.NS', 'NBI.NS', 'NCC.NS', 'NCC.NS', 'NCL.NS', 'NDL.NS', 'NDR.NS', 'NGL.NS', 'NHPC.NS', 'NHPC.NS', 'NIIT.NS', 'NIIT.NS', 'NLC.NS', 'NMDC.NS', 'NMDC.NS', 'NMDC.NS', 'NOCIL.NS', 'NOCIL.NS', 'NRB.NS', 'NRB.NS', 'NIBL.NS', 'NTPC.NS', 'NTPC.NS', 'NDGL.NS', 'NGIL.NS', 'NSIL.NS', 'NDL.NS', 'NH.NS', 'NFL.NS', 'NELCO.NS', 'NESCO.NS', 'NTL.NS', 'NDTV.NS', 'NAM.NS', 'INDIA.NS', 'NIRAJ.NS', 'NITCO.NS', 'NRL.NS', 'ONGC.NS', 'OIL.NS', 'OMAXE.NS', 'PAYTM.NS', 'OFSS.NS', 'OAL.NS', 'OCCL.NS', 'OBCL.NS', 'ORTEL.NS', 'PAE.NS', 'PAEL.NS', 'PB.NS', 'PBA.NS', 'PC.NS', 'PCBL.NS', 'PCBL.NS', 'PDS.NS', 'PDSL.NS', 'PG.NS', 'PGEL.NS', 'PI.NS', 'PIIND.NS', 'PNB.NS', 'PNB.NS', 'PNC.NS', 'PPAP.NS', 'PPAP.NS', 'PSP.NS', 'PTC.NS', 'PFS.NS', 'PTC.NS', 'PTC.NS', 'PTC.NS', 'PTCIL.NS', 'PTL.NS', 'PTL.NS', 'PVP.NS', 'PVP.NS', 'PVR.NS', 'INOX.NS', 'PAKKA.NS', 'PAR.NS', 'PARAS.NS', 'PDPL.NS', 'PGIL.NS', 'LNG.NS', 'PEL.NS', 'POCL.NS', 'PFC.NS', 'PIGL.NS', 'PPL.NS', 'PRITI.NS', 'PNC.NS', 'PGHL.NS', 'PGHH.NS', 'PSB.NS', 'PNB.NS', 'PURVA.NS', 'QUESS.NS', 'R.NS', 'R.NS', 'R.NS', 'RBL.NS', 'REC.NS', 'RHI.NS', 'RHIM.NS', 'RKEC.NS', 'RKEC.NS', 'RPG.NS', 'RPP.NS', 'RPSG.NS', 'RS.NS', 'RSWM.NS', 'RSWM.NS', 'RACE.NS', 'I.NS', 'RMCL.NS', 'RVNL.NS', 'RAIN.NS', 'ROML.NS', 'RAJTV.NS', 'RPPL.NS', 'RAMKY.NS', 'RML.NS', 'RBL.NS', 'RCF.NS', 'RKDL.NS', 'RVHL.NS', 'REC.NS', 'RHI.NS', 'RHIM.NS', 'RKEC.NS', 'RKEC.NS', 'RPG.NS', 'RPP.NS', 'RPSG.NS', 'RS.NS', 'RSWM.NS', 'RSWM.NS', 'RACE.NS', 'I.NS', 'RMCL.NS', 'RVNL.NS', 'RAIN.NS', 'ROML.NS', 'RAJTV.NS', 'RPPL.NS', 'RAMKY.NS', 'RML.NS', 'RBL.NS', 'RCF.NS', 'RKDL.NS', 'RVHL.NS', 'SBI.NS', 'SEL.NS', 'SELMC.NS', 'SEPC.NS', 'SEPC.NS', 'SIL.NS', 'SIS.NS', 'SIS.NS', 'SITI.NS', 'SJS.NS', 'SJS.NS', 'SJVN.NS', 'SJVN.NS', 'SKF.NS', 'SKIL.NS', 'SKIL.NS', 'SKM.NS', 'SMC.NS', 'SML.NS', 'SMS.NS', 'SMS.NS', 'SORIL.NS', 'SPL.NS', 'SPLIL.NS', 'SPML.NS', 'SREI.NS', 'SRF.NS', 'SRF.NS', 'SRG.NS', 'STEL.NS', 'STEL.NS', 'STL.NS', 'SGL.NS', 'SVP.NS', 'SAH.NS', 'SAKAR.NS', 'SECL.NS', 'SAMHI.NS', 'SANCO.NS', 'SMLT.NS', 'SATIA.NS', 'SATIN.NS', 'SOTL.NS', 'SELAN.NS', 'SEMAC.NS', 'SENCO.NS', 'SETCO.NS', 'SHAH.NS', 'SFL.NS', 'SCPL.NS', 'SPYL.NS', 'SMLT.NS', 'SATIA.NS', 'SATIN.NS', 'SOTL.NS', 'SELAN.NS', 'SEMAC.NS', 'SENCO.NS', 'SETCO.NS', 'SHAH.NS', 'SFL.NS', 'SCPL.NS', 'SPYL.NS', 'SDBL.NS', 'BLW.NS', 'SPIC.NS', 'SREEL.NS', 'SABTN.NS', 'SIL.NS', 'SBIN.NS', 'SAIL.NS', 'SAIL.NS', 'SSWL.NS', 'STAR.NS', 'SULA.NS', 'SUMIT.NS', 'SDBL.NS', 'BLW.NS', 'SPIC.NS', 'SREEL.NS', 'SABTN.NS', 'SIL.NS', 'SBIN.NS', 'SAIL.NS', 'SAIL.NS', 'SSWL.NS', 'STAR.NS', 'SULA.NS', 'SUMIT.NS', 'SDBL.NS', 'BLW.NS', 'SPIC.NS', 'SREEL.NS', 'SABTN.NS', 'SIL.NS', 'SBIN.NS', 'SAIL.NS', 'SAIL.NS', 'SSWL.NS', 'STAR.NS', 'SULA.NS', 'SUMIT.NS', 'ANUP.NS', 'BYKE.NS', 'FACT.NS', 'NIACL.NS', 'PKTEA.NS', 'WIPL.NS', 'THEJO.NS', 'TI.NS', 'TITAN.NS', 'TOTAL.NS', 'TRIL.NS', 'TCI.NS', 'TFL.NS', 'TRENT.NS', 'TBZ.NS', 'TRU.NS', 'UCAL.NS', 'UCAL.NS', 'UCO.NS', 'UFO.NS', 'UFO.NS', 'UNO.NS', 'UPL.NS', 'UPL.NS', 'UTI.NS', 'USK.NS', 'UFLEX.NS', 'UJAAS.NS', 'UBL.NS', 'UNIDT.NS', 'N.NS', 'UDS.NS', 'T.NS', 'URAVI.NS', 'URJA.NS', 'V.NS', 'V.NS', 'VMART.NS', 'VIP.NS', 'VIP.NS', 'VL.NS', 'E.NS', 'IT.NS', 'VLS.NS', 'VRL.NS', 'VST.NS', 'VST.NS', 'WABAG.NS', 'VHL.NS', 'VSSL.NS', 'VTL.NS', 'VBL.NS', 'VCL.NS', 'VEDL.NS', 'VETO.NS', 'WSP.NS', 'VINNY.NS', 'I.NS', 'R.NS', 'VPRPL.NS', 'IDEA.NS', 'W.NS', 'S.NS', 'WSI.NS', 'WEWIN.NS', 'WENDT.NS', 'WIPRO.NS', 'WEL.NS', 'WORTH.NS', 'YES.NS', 'YAARI.NS', 'YASHO.NS', 'YATRA.NS', 'YUKEN.NS', 'ZF.NS', 'ZEEL.NS', 'JRD.NS', 'MKJ.NS', 'ZOTA.NS', 'ZUARI.NS']




# Calculate and display returns for each stock
for stock_symbol in stocks:
    return_percentage = calculate_return(stock_symbol)
    print(f"{stock_symbol}: {return_percentage:.2f}%")