import asyncio
import logging
from modules.nectar_market import NectarMarket
from modules.nectar_intelligence import NectarIntelligence
from modules.nectar_ghost import NectarGhost
from modules.nectar_synthesis import NectarSynthesis

logging.basicConfig(level=logging.INFO, format='%(asctime)s - SOVEREIGN-INIT - %(levelname)s - %(message)s')
logger = logging.getLogger("SOVEREIGN-INIT")

class NectarSovereignty:
    def __init__(self):
        self.market = NectarMarket()
        self.intel = NectarIntelligence()
        self.ghost = NectarGhost()
        self.synth = NectarSynthesis()

    async def initialize(self):
        logger.info("Iniciando Suite de Soberania Néctar...")
        
        # Exemplo de fluxo integrado
        logger.info("Passo 1: Coletando Inteligência SOTA...")
        benchmarks = await self.intel.get_lm_arena_benchmarks()
        logger.info(f"Benchmarks sincronizados: {benchmarks['top_models']}")

        logger.info("Passo 2: Analisando Sentimento via Ghost RSE...")
        sentiment = await self.ghost.analyze_sentiment_rse(["New SOTA model release", "Massive adoption of L2"])
        logger.info(f"Sentimento de mercado: {sentiment['overall_sentiment']}")

        logger.info("Passo 3: Verificando Arbitragem Predatória...")
        opp = await self.market.analyze_predatory_opportunity("SOL", {"EX1": 145, "EX2": 147}, migration_risk=0.5)
        if opp['action'] == 'EXECUTE':
            logger.info(f"Oportunidade detectada: {opp['opportunities'][0]['spread']:.2%}")

        logger.info("Passo 4: Sincronizando com Memória Ancestral...")
        block = self.synth.distill_content(f"Sintese do dia: {sentiment['overall_sentiment']} sentiment")
        self.synth.add_to_rag(block)
        
        logger.info("Soberania Operacional.")

    async def stop(self):
        await self.market.close()
        await self.intel.close()

if __name__ == "__main__":
    async def run():
        sov = NectarSovereignty()
        await sov.initialize()
        await sov.stop()
    
    asyncio.run(run())
