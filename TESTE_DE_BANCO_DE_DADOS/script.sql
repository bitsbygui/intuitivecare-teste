CREATE DATABASE teste_db;

USE teste_db;

-- Criar a tabela para os dados financeiros
CREATE TABLE relatorio_base (
    DATA DATE,
    REG_ANS INT,
    CD_CONTA_CONTABIL VARCHAR(20),
    DESCRICAO TEXT,
    VL_SALDO_INICIAL text,
    VL_SALDO_FINAL text
);

-- Criar a tabela para os dados das operadoras
CREATE TABLE relatorio_cadop (
    Registro_ANS INT PRIMARY KEY,
    CNPJ VARCHAR(14),
    Razao_Social VARCHAR(255),
    Nome_Fantasia VARCHAR(255),
    Modalidade VARCHAR(255),
    Logradouro VARCHAR(255),
    Numero VARCHAR(20),
    Complemento VARCHAR(255),
    Bairro VARCHAR(255),
    Cidade VARCHAR(255),
    UF VARCHAR(2),
    CEP VARCHAR(10),
    DDD VARCHAR(5),
    Telefone VARCHAR(20),
    Fax VARCHAR(20),
    Endereco_eletronico VARCHAR(255),
    Representante VARCHAR(255),
    Cargo_Representante VARCHAR(255),
    Regiao_de_Comercializacao text,
    Data_Registro_ANS DATE
);

LOAD DATA INFILE 'C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/relatorio_base.csv'
INTO TABLE relatorio_base
FIELDS TERMINATED BY ';' 
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;

LOAD DATA INFILE 'C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/relatorio_cadop.csv'
INTO TABLE relatorio_cadop
FIELDS TERMINATED BY ';' 
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;

-- Maiores despesas no último trimestre
SELECT 
    c.Razao_Social, 
    SUM(CAST(b.VL_SALDO_FINAL AS DECIMAL(15,2))) AS Total_Despesas
FROM relatorio_base b
JOIN relatorio_cadop c ON b.REG_ANS = c.Registro_ANS
WHERE 
    b.DESCRICAO LIKE '%EVENTOS/ SINISTROS CONHECIDOS OU AVISADOS  DE ASSISTÊNCIA A SAÚDE MEDICO HOSPITALAR%'
    AND QUARTER(b.DATA) = QUARTER(CURDATE() - INTERVAL 3 MONTH)
    AND YEAR(b.DATA) = YEAR(CURDATE() - INTERVAL 3 MONTH)
GROUP BY c.Razao_Social
ORDER BY Total_Despesas DESC
LIMIT 10;


-- Maiores despesas no último ano
SELECT 
    c.Razao_Social, 
    SUM(CAST(b.VL_SALDO_FINAL AS DECIMAL(15,2))) AS Total_Despesas
FROM relatorio_base b
JOIN relatorio_cadop c ON b.REG_ANS = c.Registro_ANS
WHERE 
    b.DESCRICAO LIKE '%EVENTOS/ SINISTROS CONHECIDOS OU AVISADOS  DE ASSISTÊNCIA A SAÚDE MEDICO HOSPITALAR%'
    AND YEAR(b.DATA) = YEAR(CURDATE() - INTERVAL 1 YEAR)
GROUP BY c.Razao_Social
ORDER BY Total_Despesas DESC
LIMIT 10;


