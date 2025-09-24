from plone import api
from Products.CMFPlone.WorkflowTool import WorkflowTool
from Products.GenericSetup.tool import SetupTool
from tremt.intranet import logger


def atualiza_permissoes(portal_setup: SetupTool):
    """Atualiza todas as permissoes em vista do novo workflow."""
    # Utilizamos a tool que gerencia todos os workflows
    wf_tool: WorkflowTool = api.portal.get_tool("portal_workflow")
    # Atualiza permissoes
    wf_tool.updateRoleMappings()
    # Loga que modificacao foi realizada
    logger.info("Permissoes de workflow atualizadas")
