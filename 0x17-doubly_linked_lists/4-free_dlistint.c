# include "lists.h"
/**
 * free_dlistint - free memory
 * @head: headnode
 */ 
void free_dlistint(dlistint_t *head)
{
	if (head != NULL)
	{
		while (head->next != NULL)
		{
			head = head->next;
			free(head->prev);
		}
		free(head);
		head = NULL;
	}
}
