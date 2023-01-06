from fastapi import APIRouter
from config.db import conn
from sqlalchemy import text


router=APIRouter()



@router.post('/')
async def get_info(item:dict):
    stmt=text("select Usu_Cuenta,Usu_Nombre,Perfil from INDMaeUsuario where Usu_Cuenta='"+item["Usu_Cuenta"]+"' and Usu_Password='"+item["Usu_Password"]+"'")
    users=conn.execute(stmt)
    usersList=users.fetchall()
    return usersList

@router.post('/user/empresas')
async def get_empresas(item:str):
    stmt=("SELECT maeEmpresa.empCodigo, maeEmpresa.empNombre FROM INDUsuNegocio INNER JOIN maeEmpresa ON INDUsuNegocio.CtoEmpresa = maeEmpresa.empCodigo WHERE (INDUsuNegocio.Usu_Cuenta ='"+item+"')group by maeEmpresa.empCodigo, maeEmpresa.empNombre")
    empresas=conn.execute(stmt)
    empresasList=empresas.fetchall()
    return empresasList

@router.post('/user/empresas/obras')
async def get_obras(item:dict):
    stmt=("SELECT INDMaeUNegocioActivas.CtoCodigo,UPPER(INDMaeUNegocioActivas.CtoDescripcion) as Obras FROM INDMaeUNegocioActivas INNER JOIN INDUsuNegocio ON INDMaeUNegocioActivas.CtoCodigo = INDUsuNegocio.CtoCodigo AND INDMaeUNegocioActivas.CtoEmpresa = INDUsuNegocio.CtoEmpresa WHERE (INDUsuNegocio.Usu_Cuenta = '"+item["Usu_Cuenta"]+"') AND (INDUsuNegocio.CtoEmpresa = '"+item["CtoEmpresa"]+"')")
    obras=conn.execute(stmt)
    obrasList=obras.fetchall()
    return obrasList

@router.post('/user/empresas/obras/sector')
async def get_sectores(item:dict):
    stmt=("SELECT DISTINCT Sector FROM INDTrUnidadFisica WHERE (CtoEmpresa = '"+item["CtoEmpresa"]+"') AND (CtoCodigo = '"+item["CtoCodigo"]+"') AND (Sector <> 0)")
    sector=conn.execute(stmt)
    sectorList=sector.fetchall()
    return sectorList

@router.post('/user/empresas/obras/ufisica')
async def get_sectores(item:dict):
    stmt=("SELECT unidadfisica  FROM INDTrUnidadFisica where CtoEmpresa='"+item["CtoEmpresa"]+"' and CtoCodigo='"+item["CtoCodigo"]+"' and sector='"+item["sector"]+"' and Sector<>0 ORDER BY unidadfisica ASC")
    uFisica=conn.execute(stmt)
    uFisicaList=uFisica.fetchall()
    return uFisicaList